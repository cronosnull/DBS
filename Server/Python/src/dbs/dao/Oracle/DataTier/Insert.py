#!/usr/bin/env python
""" DAO Object for DataTiers table """ 

from WMCore.Database.DBFormatter import DBFormatter
from dbs.utils.dbsExceptionHandler import dbsExceptionHandler

class Insert(DBFormatter):

    def __init__(self, logger, dbi, owner):
            DBFormatter.__init__(self, logger, dbi)
	    self.owner = "%s." % owner if not owner in ("", "__MYSQL__") else ""
	    
            self.sql = """INSERT INTO %sDATA_TIERS ( DATA_TIER_ID, DATA_TIER_NAME, CREATION_DATE, CREATE_BY) VALUES (:data_tier_id, :data_tier_name, :creation_date, :create_by)""" % (self.owner)

    def execute( self, conn, dtObj, transaction=False, cache=None ):
	result = self.dbi.processData(self.sql, dtObj, conn, transaction)
	# Now attempt to set this in cache
        if cache:
                cachedDataTiers=cache.get("DATA_TIERS")
                cachedDataTiers = cachedDataTiers if cachedDataTiers!= None else []
                cachedDataTiers.append(dtObj)
		cache.set("DATA_TIERS", cachedDataTiers)
	return


