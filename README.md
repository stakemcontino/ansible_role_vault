## Ansible Role Vault

[![Build Status](https://travis-ci.org/stakemcontino/ansible_role_vault.svg?branch=master)](https://travis-ci.org/stakemcontino/ansible_role_vault)
Ansible role in install hashicorp vault

## Requirements

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

## Role Variables

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - role: ansible_role_vault

## Molecule

The full documentation can be found [here](http://molecule.readthedocs.io/en/latest/)

### Assumptions

You have ansible, docker and python 2.7 installed

### Prerequisites

Create a python virtualenv (not essential, but recommended)
    virtualenv -p /usr/local/bin/python2.7 venv
    source venv/bin/activate
    pip install ansible 'docker<3.0.0' molecule

### For the impatient - tl;dr

Just run this
   cd ansible_role_vault && molecule test

### Breaking down what happens in the command above

[Molecule Lint](http://molecule.readthedocs.io/en/latest/usage.html#lint)

Out of the box, molecule lint runs 3 tasks:
1. https://yamllint.readthedocs.io/en/latest/
2. https://github.com/willthames/ansible-lint
3. http://flake8.pycqa.org/en/latest/

To run molecule lint
    cd ansible_role_vault
    molecule lint

[Molecule Create](http://molecule.readthedocs.io/en/latest/usage.html#create)

Creates an instance, in this case a docker machine to test the ansible role.

To run molecule create
    molecule create

[Molecule Converge](http://molecule.readthedocs.io/en/latest/usage.html#converge)

Takes the docker instance created above and runs the molecule/default/playbook.yml
    molecule converge

[Molecule Idempotence](https://molecule.readthedocs.io/en/latest/usage.html#idempotence)

Checks the role is idempotent, typically it will identify tasks that use run commands (shell, command, raw, script) instead of a module.
    molecule idempotence

[Molecule verify](https://molecule.readthedocs.io/en/latest/usage.html#verify)

Verify will run any tests that are defined in molecule/default/tests/test_default.py
    molecule verify

[Molecule verify](https://molecule.readthedocs.io/en/latest/usage.html#destroy)

Teardown what had was created in the steps above
    molecule destroy

Link to [Travis](https://travis-ci.org/stakemcontino/ansible_role_vault)

## License

BSD

## Author Information

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
