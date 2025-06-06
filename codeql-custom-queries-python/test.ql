import python
import semmle.python.dataflow.new.RemoteFlowSources

// select any(RemoteFlowSource rfs) // select any RemoteFlowSource appearance

from Call call
select call.getFunc().(Name).getId(), "Found a call to put_item"