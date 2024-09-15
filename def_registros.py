# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 20:47:20 2020

@author: smonteiro
"""
# -----------------------------------------------------------------------------
# Essa classe possui métodos CRUD
# -----------------------------------------------------------------------------
import psycopg2


class AppBD:
    def __init__(self):
        print('Método Construtor')

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="cruzeiro",
                                               host="localhost",
                                               dbname="postgres")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)

    # -----------------------------------------------------------------------------
    # Selecionar todos os Produtos
    # -----------------------------------------------------------------------------
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Selecionando todos os produtos")
            sql_select_query = """select * from "registro" """

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)


        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)

        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
        return registros

    # -----------------------------------------------------------------------------
    # Inserir Produto
    # -----------------------------------------------------------------------------
    def inserirDados(self, codigo, data, nome, turma):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """ INSERT INTO "registro" 
          ("codigo", "data", "nome", "turma") VALUES (%s,%s,%s,%s)"""
            record_to_insert = (codigo, data, nome, turma)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com successo na tabela PRODUTO")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao inserir registro na tabela PRODUTO", error)
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    # -----------------------------------------------------------------------------
    # Atualizar Produto
    # -----------------------------------------------------------------------------
    def atualizarDados(self, codigo, data, nome, turma):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Registro Antes da Atualização ")
            sql_select_query = """select * from "registro" 
            where "codigo" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
            # Atualizar registro
            sql_update_query = """Update "registro" set "nome" = %s, "data" = %s, 
            "turma" = %s where "codigo" = %s"""
            cursor.execute(sql_update_query, (nome, data, turma, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso! ")
            print("Registro Depois da Atualização ")
            sql_select_query = """select * from "registro" 
            where "codigo" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    # -----------------------------------------------------------------------------
    # Excluir Produto
    # -----------------------------------------------------------------------------
    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            # Atualizar registro
            sql_delete_query = """Delete from "registro" 
            where "codigo" = %s"""
            cursor.execute(sql_delete_query, (codigo,))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso! ")
        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    # -----------------------------------------------------------------------------

    def buscarDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_select_query = """select * from "registro" where "codigo" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            return record

        except (Exception, psycopg2.Error) as error:
            print('Erro na Busca', error)
        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()
                print('A conecxão com o PostegreSQL foi fechada')












