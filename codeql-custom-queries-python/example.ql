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

predicate isOsEnvironSubscript(Subscript sub) {
  sub.getValue() instanceof Attribute and
  sub.getValue().(Attribute).getAttr() = "environ" and
  sub.getValue().(Attribute).getValue() instanceof Name and
  sub.getValue().(Attribute).getValue().(Name).getId() = "os"
}

module EnvToFileConfiguration implements DataFlow::ConfigSig {
  predicate isSource(DataFlow::Node source) {
    source = API::moduleImport("os").getMember("getenv").getACall()
    or
    source = API::moduleImport("os").getMember("environ").getMember("get").getACall()
    or
    exists(Subscript sub | isOsEnvironSubscript(sub) and source.asExpr() = sub)
  }

  predicate isSink(DataFlow::Node sink) { sink = any(FileSystemAccess fa).getAPathArgument() }
}

module EnvToFileFlow = TaintTracking::Global<EnvToFileConfiguration>;

from DataFlow::Node input, DataFlow::Node fileAccess
where EnvToFileFlow::flow(input, fileAccess)
select fileAccess.asCfgNode(), "This file access uses data from $@", input.getLocation(), "Filesystem Access from Envrionment Variables"

