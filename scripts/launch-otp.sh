java -Xmx4G -jar otp-0.19.0-shaded.jar --server --basePath otp --router nyc --graphs otp/graph/

java -cp "otp-0.19.0-shaded.jar;jython-standalone-2.7.0.jar" org.opentripplanner.standalone.OTPMain --server --basePath otp --router nyc --graphs otp/graph/ --enableScriptingWebService