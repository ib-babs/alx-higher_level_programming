#!/bin/bash
# Display HTTP Status code
curl -so /dev/null -w "%{http_code}" "$1"
