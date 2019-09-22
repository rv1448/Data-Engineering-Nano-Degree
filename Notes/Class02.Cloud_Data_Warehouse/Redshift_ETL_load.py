"""Load FACT and Dimension with and without DIST and SORT keys """

def load(schema,tables):
    """
    Description: Loads for given set of tables for a given Schema

    Parameters:
    ----------
    Schema: String
    dist or no dist

    Returns:
    -------
    Returns Data frame with tablename and time taken to load the table
    """
    loadtime = []
    query = """
            copy {} from s3://{} 
            credentials 'aws_iam_role = {}'
            """
    for table in tables:
        qry = query.format(table,table,DWH_IAM_ROLE)
        t0 = time()
        %sql $qry
        t1 = time()

        loadtime.append(t1-t0)
    return pd.DataFrame({"tablename": tables, "load_"+schema: loadtime}).set_index('tablename')


