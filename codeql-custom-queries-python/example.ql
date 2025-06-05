/**
 * This is an automatically generated file
 *
 * @name Hello world
 * @kind problem
 * @problem.severity warning
 * @id python/example/hello-world
 */

import python
import semmle.python.dataflow.new.DataFlow
import semmle.python.dataflow.new.TaintTracking
import semmle.python.dataflow.new.RemoteFlowSources
import semmle.python.ApiGraphs
import semmle.python.Concepts

module EnvToFileConfiguration implements DataFlow::ConfigSig {
  predicate isSource(DataFlow::Node source) {
    source = API::moduleImport("os").getMember("getenv").getACall()
  }

  predicate isSink(DataFlow::Node sink) { sink = any(FileSystemAccess fa).getAPathArgument() }
}

module EnvToFileFlow = TaintTracking::Global<EnvToFileConfiguration>;

from DataFlow::Node input, DataFlow::Node fileAccess
where EnvToFileFlow::flow(input, fileAccess)
select fileAccess, "This file access uses data from $@.", input, "user-controllable input."
