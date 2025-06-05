import python

from Subscript subscript, Expr idx
where
  subscript.getValue() instanceof Attribute and
  subscript.getValue().(Attribute).getAttr() = "environ" and
  subscript.getValue().(Attribute).getValue() instanceof Name and
  subscript.getValue().(Attribute).getValue().(Name).getId() = "os" and
  idx = subscript.getIndex()
select subscript.getValue(), "Access to os.environ with key: " + idx
