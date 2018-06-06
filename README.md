# FAIRshake

A web interface for the scoring of biomedical digital objects by user evaluation according to the FAIR data principles: Findability, Accessibility, Interoperability, and Reusability.

## Project Layout
- `app`: Application primary namespace, modules are recursively imported for inversion of control registration
  - `entities`: Implementations of abstract interfaces. Should only ever depend on abstractions in `interfaces`, not directly on other `entities`.
  - `interfaces`: Abstract interfaces to be implemented. API interfaces define the swagger spec in the same place for close coupling.
  - `util`: Application-independent utility functions for code-reuse
- `tests`: Nose tests for verifying entities properly implement their interface and general app functionality.
  - `test_util`: Nose tests for verifying that utilities work as anticipated.

## Development

### Setting up environment
Python version of >= 3.5 is recommended, type annotation support is required.
Install dependencies with `pip install -r requirements.txt`.

### Run FAIRshakeWeb server
`python run.py`

### Run Application Tests
`nosetests`

### Run Application Static Type Checks
`mypy`
