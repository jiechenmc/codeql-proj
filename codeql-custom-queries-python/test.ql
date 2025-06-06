import python

/**
 * Finds any call where the receiver is an S3 resource variable.
 */
from Call call
where 
      // call.getFunc() instanceof Attribute and
      // call.getFunc().(Attribute).getAttr().regexpMatch(".*put.*") and
      // call.getFunc().(Attribute).getValue() instanceof Name and // getValue returns os in os.getenv()
      call.getFunc().(Attribute).getValue().(Name).getId() = "s3" // does not track something like s3 = boto3.resource('s3')
select "Call to S3 resource method: " + call.getFunc().(Attribute).getValue().(Name).getId()
