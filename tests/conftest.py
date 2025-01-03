import os
import sys

# So that we can do `import swarmnode` in our tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import swarmnode  # noqa: E402

swarmnode.api_base = os.getenv("SWARMNODE_API_BASE")  # type: ignore
swarmnode.api_key = os.getenv("SWARMNODE_API_KEY")  # type: ignore
