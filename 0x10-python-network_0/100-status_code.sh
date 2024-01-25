#!/bin/bash
# Display HTTP Status code
curl -I -s -o /dev/null -w "%{http_code}"