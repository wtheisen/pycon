#!/bin/bash

set -e                          # exit immediately on error
set -x                          # print commands as they execute

python manage.py loaddata \
  fixtures/auth_user.json \
  fixtures/initial_data.json \
  fixtures/pycon.json \
  fixtures/cms_initial_pages.json \
  fixtures/conference.json \
  fixtures/initial_boxes.json \
  fixtures/initial_data.json \
  fixtures/proposal_base.json \
  fixtures/sitetree_menu.json \
  fixtures/sponsorship_benefits.json \
  fixtures/sponsorship_levels.json \
  fixtures/tutorials_schedule.json \
  fixtures/talks_schedule.json \
  fixtures/permissions.json \
  fixtures/teams.json \

echo
echo
echo "Database initialized."
echo "Hint: setup an account with: ./manage.py createsuperuser"
