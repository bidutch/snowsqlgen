# SnowSqlGen

This repository contains basic Python scripting made with the purpose of working on my Python skills and at the same time generating some SQL code that I can implement in my Snowflake database

The Links.md file contains some of the stuff that i stumbled upon while using Stackoverflow and Google for inspiration.

The dialect generated with this script is purely for the Snowflake database.

The output file naming convention is based upon the CI/CD framework Snowchange.

Extensive documentation on Snowchange can be found in the repository at ,but the command to deploy is lke this:

python cli.py -a zu82445.west-europe.azure -u johan -r SYSADMIN -w COMPUTE_WH

Make sure you enroll for a 30 day trial for this purpose at https://signup.snowflake.com/