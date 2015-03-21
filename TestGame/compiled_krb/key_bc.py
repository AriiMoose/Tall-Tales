# key_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def take(rule, arg_patterns, arg_context):
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
        with engine.prove('key_facts', 'inChest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "key.take: got unexpected plan from when clause 1"
            from Scenes import demoScene
            demoScene.DemoScene.demo_player.textComp.output_string = "You cannot take the key"
            if demoScene.DemoScene.has_key is True:
                demoScene.DemoScene.demo_player.textComp.output_string = "You already have the key"
            elif demoScene.DemoScene.has_key is False and demoScene.DemoScene.key_present is True:
                demoScene.DemoScene.demo_player.textComp.output_string = "You take the key"
                demoScene.DemoScene.has_key = True
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def eat(rule, arg_patterns, arg_context):
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
        if demoScene.DemoScene.has_key is True:
            demoScene.DemoScene.demo_player.textComp.output_string = "You eat the key"
            demoScene.DemoScene.has_key = False
            demoScene.DemoScene.key_present = False
            demoScene.DemoScene.key_eaten = True
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def poop(rule, arg_patterns, arg_context):
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
        if demoScene.DemoScene.key_eaten and demoScene.DemoScene.key_eaten is True:
            demoScene.DemoScene.demo_player.textComp.output_string = "You poop out the key"
            demoScene.DemoScene.has_key = False
            demoScene.DemoScene.key_present = True
            demoScene.DemoScene.key_eaten = False
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def drop(rule, arg_patterns, arg_context):
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
        if demoScene.DemoScene.has_key is True:
            demoScene.DemoScene.demo_player.textComp.output_string = "You drop the key on the floor"
            demoScene.DemoScene.has_key = False
        else:
            demoScene.DemoScene.demo_player.textComp.output_string = "You don't have the key"
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('key')
  
  bc_rule.bc_rule('take', This_rule_base, 'take',
                  take, None,
                  (),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('eat', This_rule_base, 'eat',
                  eat, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('poop', This_rule_base, 'poop',
                  poop, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('drop', This_rule_base, 'drop',
                  drop, None,
                  (),
                  (),
                  ())


Krb_filename = '../KB/key.krb'
Krb_lineno_map = (
    ((16, 20), (4, 4)),
    ((22, 27), (6, 6)),
    ((28, 34), (7, 17)),
    ((47, 51), (20, 20)),
    ((53, 58), (22, 29)),
    ((71, 75), (31, 31)),
    ((77, 82), (33, 40)),
    ((95, 99), (42, 42)),
    ((101, 106), (44, 51)),
)
