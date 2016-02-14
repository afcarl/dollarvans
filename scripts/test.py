#!/usr/bin/jython - courtesy: https://github.com/laurentg/otp-travel-time-matrix
# clayton@clayton-galago-ultrapro:~/otp$ jython -Dpython.path=otp-0.19.0-shaded.jar ~/Documents/CUSP/GRA_opps/DF_GRA/DCP_Project/OTP_Analysis/test.py
#from org.opentripplanner.scripting.api import OtpsEntryPoint

# Instantiate an OtpsEntryPoint
#otp = OtpsEntryPoint.fromArgs(['--graphs', 'otp/graph/',
#                               '--router', 'nyc'])

#otp = OtpsEntryPoint.fromArgs(['--router', 'nyc'])


# Start timing the code
import time
start_time = time.time()

# Get the default router
router = otp.getRouter('nyc')

# Create a default request for a given time
req = otp.createRequest()
req.setDateTime(2016, 2, 17, 8, 00, 00)
# req.setArriveBy(True) # this active makes router.plan() through an error at "org.opentripplanner.routing.impl.StreetVertexIndexServiceImpl.getSampleVertexAt(StreetVertexIndexServiceImpl.java:597)"
req.setMaxTimeSec(30000)
req.setModes('WALK,TRANSIT')

# The file points.csv contains the columns GEOID, X and Y.
start = otp.loadCSVPopulation('data/csv/start.csv', 'lat', 'lon') 
end = otp.loadCSVPopulation('data/csv/end.csv', 'lat', 'lon')

# Create a CSV output
matrixCsv = otp.createCSVOutput()
# matrixCsv.setHeader([ 'o_code', 'o_lat', 'o_lon', 'd_code', 'd_lat', 'd_lon', 'Walk_distance', 'Travel_time'])
matrixCsv.setHeader(['o_code', 'd_code', 'walk_dist', 'travel_seconds'])

print 'starting analysis'
# Start Loop
for origin in start:
    print origin
    # print "Processing origin: ", origin
    req.setOrigin(origin)
    spt = router.plan(req)
    if spt is None:
        print "ahh"
        continue

    # Evaluate the SPT for all points
    result = spt.eval(end)
    #o_loc = spt.getSnappedOrigin()
    #o_lat = o_loc.getLat()
    #o_lon = o_loc.getLon()
  
  # Add a new row of result in the CSV output
    print result
    for r in result:
        print dir(r)
        #resIndv = r.getIndividual()
        #d_loc = resIndv.getSnappedLocation()
        #matrixCsv.addRow([ origin.getStringData('blk_num'), o_lat, o_lon, resIndv.getStringData('blk_num'), d_loc.getLat(), d_loc.getLon(), r.getWalkDistance(), r.getTime(), r.getBoardings()])
        matrixCsv.addRow([ origin.getStringData('blk_num'), r.getIndividual().getStringData('blk_num'), r.getWalkDistance(), r.getTime()])

# Save the result
matrixCsv.save('test_block_traveltime_v2.csv')

# Stop timing the code
print("Elapsed time was %g seconds" % (time.time() - start_time))
