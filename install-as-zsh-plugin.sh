mkdir -p ~/.oh-my-zsh/custom/plugins/folder-categorizer/
cp folder-categorizer.plugin.zsh ~/.oh-my-zsh/custom/plugins/folder-categorizer/
pyinstaller --onefile folder-categorizer.py
cp dist/folder-categorizer ~/.oh-my-zsh/custom/plugins/folder-categorizer