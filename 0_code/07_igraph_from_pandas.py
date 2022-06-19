# turn this into a function
def igraph_from_pandas(edges_table, vertices_table, source_cl='from', target_cl='to', vertex_attrs=None, vertex_id_cl='v_id', directed=False):
    """igraph_from_pandas(edges_table, vertices_table, source_cl='from', target_cl='to', vertex_attrs=None, vertex_id_cl='v_id', directed=False)
    
    Takes two pandas dataframes, vertices and edges tables, and builds igraph graph including both vertex and edge attributes. (imports pandas as pd and igraph as ig, they should be installed).
    
    @param edges_table: Pandas dataframe with two columns as "from" and "to" nodes of each edge. If name of columns are different, they should to be declared using following parameters.
    @param vertices_table:
    @param source_cl: Name of column including starting nodes of each edge defaults to "from".
    @param target_cl: Name of column including ending nodes of each edge defaults to "to".
    @param vertex_attrs: List of pandas column names to be used as node attributes to be added to graph. Defaults to None as no attribute is needed and node names are taken from edges_table (if string) and adds to graph as "name" (e.g., g.vs['name']. If you want all vertices table columns to be used, pass list(vertices_table.columns)
    @param vertex_id_cl: Name of column in vertices_table which includes vertices names to be used while adding attributes. Defaults to "v_id".
    @param directed: bool, should the network be directed? It is passed to igraph.Graph. Defaults to False.
    
    """
    
    import pandas as pd
    import igraph as ig
    # control parameters
    if isinstance(edges_table, pd.DataFrame):
        try:
            if source_cl and target_cl in edges_table.columns:
                id_gen = ig.UniqueIdGenerator()
                edgelist = []
                for start_edge, end_edge in edges_table[[source_cl, target_cl]].itertuples(index=False, name=None):
                    edgelist.append((id_gen[start_edge], id_gen[end_edge]))
                if directed:
                    gg = ig.Graph(edgelist, directed=True)
                else:
                    gg = ig.Graph(edgelist, directed=False)
                gg.vs["name"] = id_gen.values()
        except (KeyError, NameError):
            raise ValueError('Edges columns missing!')
    else:
        raise ValueError("edges table is required!")
    if isinstance(vertices_table, pd.DataFrame):
        if not vertex_attrs:
            raise ValueError('No attributes provided. Remove vertices table from arguments and try again.')
        else:
            try:
                # order vertices table based on edge_list
                vertices_table_ordered = pd.DataFrame(id_gen.values(), columns=['unique_id'])
                # bring previous vertices table with attributes (to be reordered)
                vertices_table_ordered = vertices_table_ordered.merge(vertices_table, left_on = 'unique_id', right_on = vertex_id_cl, how='left')
                for attr2use in vertex_attrs:
                    if attr2use in vertices_table.columns:
                        # add attributes to graph
                        gg.vs[attr2use] = vertices_table_ordered[attr2use].values.tolist()
            except (KeyError, NameError):
                raise ValueError('Vertex ID column missing!')    
    return gg
