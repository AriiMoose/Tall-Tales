# chest_rules_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def open(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('chest', 'closed', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('chest', 'closed',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('chest_rules')
  
  fc_rule.fc_rule('open', This_rule_base, open,
    (('chest', 'closed',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(False),))


Krb_filename = '../KB/chest_rules.krb'
Krb_lineno_map = (
    ((13, 17), (5, 5)),
    ((18, 19), (7, 7)),
)
