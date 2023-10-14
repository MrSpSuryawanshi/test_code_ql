import python
from DataFlow::TaintSink sink
where
  sink.getTaintKind() = DataFlow::SQLInjection
select sink
