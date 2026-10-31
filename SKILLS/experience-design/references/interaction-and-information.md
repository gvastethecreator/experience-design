# Interaction, information architecture, and states

## Model before screen

Identify domain objects, who owns them, which actions they support, what scope each action has, and which states persist. Map main routes, deep entry points, return, and exits. Use verbs that distinguish save, publish, apply, and export. Make the boundaries between document, project, account, and device explicit.

Design states and transitions together with layouts. For each costly transition specify precondition, trigger, local change, remote effect, feedback, focus, rollback, and recovery. A pending state is not success. A partial failure keeps the identity of completed and pending items.

## Useful density

In expert tools, compare the cost of scanning visible information with the cost of finding it in menus or remembering it. Progressive disclosure is useful for what is infrequent or contextual, not an excuse to hide what is central. Keep frequent commands, selection, mode, and state close to the edited artifact. Evaluate keyboard access and discoverable shortcuts.

For first uses, offer examples and guidance at the point of need. For returns, restore relevant context. Avoid personalization that changes locations during a task. The contracts recommended here rely on NN-COMPLEX, NN-MODEL, and NN-ACTIVE, but they need local testing.

## Patterns to inspect by risk

**Forms:** persistent labels, requirement and format before the error, preserved values, identifiable errors, and correction without redoing everything. Immediate validation only when there is enough information; do not punish someone who is still typing.

**Search and selection:** visible scope, distinguishable names, reversible filters, and a difference between no data, no results, missing permission, and failure. A bulk action states how many items it selects, including items outside the page or filter.

**Save/import/export:** distinguish local and remote changes, expected output, name conflicts, formats, overwriting, and a verifiable result. Do not show a download as completed just because its generation started.

**Destructive actions:** keep context and specify object/consequence. Undo only if it actually reverts. If it cannot be reverted, describe the limits and require proportional review. Separate authentication from consent to the scope.

**Collaboration:** expose conflicts, versions, and concurrent editing when relevant. Do not overwrite silently. Explain who can view and modify each artifact.

## Application examples, not product audits

Visual editor: save, export, and select a region are different contracts. System cleanup: analyze, select, execute, and recover must not be a single opaque button. Music studio: avoid interruptions that alter playback, mode, or selection. Asset library: differentiate file, category, version, and approval state.

These scenarios are domain examples; they do not claim defects in an uninspected repository.

## Minimum delivery

A transition is delivered with trigger, scope, resulting state, and test. A material journey adds relevant failure states and a data contract. Add a diagram, table, or prototype only when it reduces a real ambiguity. For one or two states, precise prose can be enough.
