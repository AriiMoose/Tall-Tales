# door_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def open(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('door_facts', 'closed', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "door.open: got unexpected plan from when clause 1"
            from Scenes import demoScene
            if demoScene.DemoScene.door_open is True:
                demoScene.DemoScene.demo_player.textComp.output_string = "The door is already open"
            elif demoScene.DemoScene.door_open is False and demoScene.DemoScene.has_key is False:
                demoScene.DemoScene.demo_player.textComp.output_string = "The door is locked"
            elif demoScene.DemoScene.door_open is False and demoScene.DemoScene.has_key is True:
                demoScene.DemoScene.demo_player.textComp.output_string = "You open the door"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def kick(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        from Scenes import demoScene
        if demoScene.DemoScene.door_open is True:
            demoScene.DemoScene.demo_player.textComp.output_string = "You kick the door closed"
            demoScene.DemoScene.door_open = False
        elif demoScene.DemoScene.door_open is False and demoScene.DemoScene.has_key is False:
            demoScene.DemoScene.demo_player.textComp.output_string = "You kick the door. It's locked shut"
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('door')
  
  bc_rule.bc_rule('open', This_rule_base, 'open',
                  open, None,
                  (),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('kick', This_rule_base, 'open',
                  kick, None,
                  (),
                  (),
                  ())


Krb_filename = '../KB/door.krb'
Krb_lineno_map = (
    ((16, 20), (4, 4)),
    ((22, 27), (6, 6)),
    ((28, 34), (7, 16)),
    ((47, 51), (19, 19)),
    ((53, 58), (21, 28)),
)
