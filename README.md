### Getting Started

## Setting Up Open Trip Planner

1. Download [OTP](http://maven.conveyal.com.s3.amazonaws.com/org/opentripplanner/otp/0.19.0/otp-0.19.0-shaded.jar) to the root of the `dollarvans` repository.
2. Download [Jython](http://search.maven.org/remotecontent?filepath=org/python/jython-standalone/2.7.0/jython-standalone-2.7.0.jar) to the same directory.
3. Create a directory `nyc_data` with the transit network data.
4. Build the OTP graph by running: ```java -Xmx4G -jar otp-0.19.0-shaded.jar --build nyc_data```
5. This will create a `Graph.obj` file in `nyc_data`.  Move that file to `otp/graph/nyc`.

## Launching OTP

Start OTP by running the following from the root of the repository:

    java -cp "otp-0.19.0-shaded.jar;jython-standalone-2.7.0.jar" org.opentripplanner.standalone.OTPMain --server --basePath otp --router nyc --graphs otp/graph/ --enableScriptingWebService

## Running Scripts

Now scripts can be run by executing the following:

    curl --form "scriptfile=@scripts/test.py" localhost:8080/otp/scripting/run
