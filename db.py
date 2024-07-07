import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = None
        self.cur = None

    def connect(self):
        self.con = sqlite3.connect(self.db_name)
        self.con.execute("PRAGMA foreign_keys = ON")
        self.cur = self.con.cursor()

    def close(self):
        if self.con:
            self.con.close()

    def create_tables(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            id_usuario INTEGER PRIMARY KEY,
            nickName TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            nombre_usuario TEXT NOT NULL,
            apellido_usuario TEXT NOT NULL,
            email_usuario TEXT NOT NULL
        )
    ''')

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS tipo_cliente(
            id_type INTEGER PRIMARY KEY,
            tipo TEXT NOT NULL
        )
        ''')
        
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS clientes(
            id_cliente INTEGER PRIMARY KEY,
            run TEXT NOT NULL UNIQUE,
            nombre_cliente TEXT NOT NULL,
            apellido_cliente TEXT NOT NULL,
            direccion TEXT NOT NULL,
            telefono INTEGER NOT NULL,
            email_cliente TEXT NOT NULL,
            id_type INTEGER NOT NULL,
            FOREIGN KEY (id_type) REFERENCES tipo_cliente(id_type)
        )
        ''')

    def insert_data(self, table, columns, data):
        placeholders = ','.join(['?'] * len(columns))
        sql = f'''
        INSERT INTO {table} ({','.join(columns)})
        VALUES ({placeholders})
        '''
        self.cur.executemany(sql, data)

    def commit(self):
        self.con.commit()

    def rollback(self):
        if self.con:
            self.con.rollback()

def main():
    db = DatabaseManager("ejercicio.db")
    
    try:
        db.connect()
        
        db.create_tables()
        
        if 
        tipo_clientes = [
            ('12345678-9', 'Juan', 'Pérez', 'Calle Falsa 123', 987654321, 'juan.perez@example.com', 1),
            ('98765432-1', 'Ana', 'García', 'Avenida Siempre Viva 742', 123456789, 'ana.garcia@example.com', 2)
        ]
        db.insert_data('clientes', clientes)
        
        # Confirmar la transacción
        db.commit()
        
    except sqlite3.Error as e:
        print("Error SQLite:", e)
        db.rollback()  # Revertir todos los cambios si ocurre un error
    
    finally:
        # Cerrar la conexión
        db.close()

if __name__ == "__main__":
    main()