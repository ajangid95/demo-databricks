# Databricks notebook source
# MAGIC %sql
# MAGIC Select "Hello world from SQL"

# COMMAND ----------

_sqldf

# COMMAND ----------

# MAGIC %run ./sample
# MAGIC

# COMMAND ----------

print(name)

# COMMAND ----------

# MAGIC %fs ls "databricks-datasets"

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

display(dbutils.fs.ls("/databricks-datasets"))

# COMMAND ----------



# COMMAND ----------


