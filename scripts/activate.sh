#!/bin/sh
PI_VENV="pi"
PI_USER="$USER"
PI_HOST="raspberrypi.local"

source "${PI_VENV}-venv/bin/activate"

update() {
	PROJECT="$1"
	REMOTE="$PI_USER@$PI_HOST:~/$PROJECT"

	echo "Updating remote project '$REMOTE' with '$PROJECT'\n"
	rsync -av "$PROJECT"/. "$REMOTE/"
	ssh "$PI_USER@$PI_HOST" "cd ${PROJECT} && source ${PROJECT}-venv/bin/activate && python3 -u ${PROJECT}.py"
}
