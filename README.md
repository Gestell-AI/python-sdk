# Gestell Python SDK

![license](https://img.shields.io/badge/license-MIT-blue)
![version](https://img.shields.io/badge/version-1.0.0-blue)
[![Coverage Status](https://coveralls.io/repos/github/Gestell-AI/python-sdk/badge.svg?branch=master)](https://coveralls.io/github/Gestell-AI/python-sdk?branch=master)
[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/7sUmZuDYQ6cd8WbCiCCnfR/4vJwvhbzy5DseAhXZ59L2t/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/7sUmZuDYQ6cd8WbCiCCnfR/4vJwvhbzy5DseAhXZ59L2t/tree/master)

A fully featured SDK with extensive code completion and typesystems for interacting with the Gestell Platform. Full featured support for Python 3.X. Uses asynchronous coroutines by design.

![Project Preview](https://github.com/Gestell-AI/python-sdk/blob/master/preview.gif?raw=true)

## Quick Start

First, get an API Key from <https://platform.gestell.ai>. Then install `gestell`:

```bash
pip install gestell
```

Or...

```bash
uv add gestell
```

Second, load the API Key into your terminal session, or, pass it into the SDK:

```bash
# Load it into your terminal session
export GESTELL_API_KEY = "..."
```

Or load it directly in the client:

```python
import asyncio
from gestell import Gestell


async def main():
    gestell = Gestell(key='...', url='...', debug=True)

if __name__ == '__main__':
    asyncio.run(main())
```

**Gestell will also read and load these environment variables from a `.env` file.**

Finally, start using the Gestell Platform SDK. The SDK can be used both on the client and server side. A public facing app should use it server side only due to the API Key being passed into the SDK and requests:

```python
import asyncio
from gestell import Gestell


async def main():
    gestell = Gestell()
    try:
        list_response = await gestell.collection.list()
        print("Collections:")
        print(list_response)
    except Exception as e:
        print(f"Error listing organizations: {e}")


if __name__ == "__main__":
    asyncio.run(main())
```

## Guides

You can review guides on common workflows and use cases for the Gestell Platform by going to <https://gestell.ai/docs>. Here are the most common use cases:

1. [Create a collection and upload documents to it](https://gestell.ai/docs/quick-start)

2. [Prompt a collection](https://gestell.ai/docs/prompt)

3. [Gather all labels from a collection](https://gestell.ai/docs/labels)

4. [Gather all tables from a collection](https://gestell.ai/docs/tables)

## Contributing

All workflows in the SDK use the [ruff](https://github.com/astral-sh/ruff) and [uv](https://github.com/astral-sh/uv).

Opening an issue to address your concern is recommended. However, if you plan to submit a pull request (PR), please adhere to the following:

 1. **Align with the Repo Structure**: Organize canonical functionality within the appropriate folders. Provide clear documentation and usage annotations in the base class structures.

 2. **Pass All Unit Tests**: Ensure all `pytest` unit tests pass and maintain near full code coverage.

 3. **Provide a Detailed PR Description**: Clearly outline the changes made and the specific issues they resolve in your pull request.

The workflow is as follows:

```bash
# Compile a new dist
uv venv
uv build

# Run unit tests
ruff check
ruff format
uv run pytest
uv run coveralls

# Verify and test the package externally with uv and a normal venv environment
cd ..
uv init test
cd test
uv add ../python-sdk
uv pip install ../python-sdk/dist/gestell-1.0.0-py3-none-any.whl
```