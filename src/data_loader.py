import os
import pandas as pd
import sqlalchemy
from dotenv import load_dotenv

load_dotenv()

# Call the connection function to get the string
def mysql_conn():
    USER=os.getenv("MYSQL_USER")
    PASSWORD=os.getenv("MYSQL_PASSWORD")
    HOST=os.getenv("MYSQL_HOST")
    PORT=os.getenv("MYSQL_PORT")
    DATABASE=os.getenv("MYSQL_SCHEMA")



   
    mysql_connection_string = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

    return mysql_connection_string


def load_csv_into_db(csv_path, table_name):
    """Read CSV and load to MYSQL database."""
    # Check if the connection string string was generated properly
    conn_string = mysql_conn()

    if not conn_string:
        print("✗ Error: Connection string is None. Check your config.py file.")
        return False
        
    try:
        df = pd.read_csv(csv_path)
        print(f"✓ CSV loaded successfully. Shape: {df.shape}")
        print(f"Columns: {df.columns.tolist()}")
        
        # Create database engine
        engine = sqlalchemy.create_engine(conn_string)
        
        # Load data into table using the passed table_name parameter
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        
        print("Data loaded successfully.")
        
        # Get the row count directly from the dataframe
        nrows = df.shape[0]
        print(f"✓ Successfully loaded {nrows} rows into {table_name}")
        
        # SQLalchemy engines use dispose() instead of close()
        engine.dispose()
        return True
    
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

if __name__ == "__main__":
    # Example usage
    csv_path = os.getenv('DATA_PATH', r"E:\python_project_demo\data\sample_data.csv")
    target_table = "mysql_test"
    
    load_csv_into_db(csv_path, target_table)
