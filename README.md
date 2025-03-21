# DiscordBot-GithubIssues

A Discord bot that helps bridge the gap between Discord conversations and GitHub issue tracking. This bot allows users to create GitHub issues directly from Discord and view existing issues in repositories.

## Features

### Current Functionality

- **Create GitHub Issues**: Generate links to create new issues in GitHub repositories directly from Discord
- **View Open Issues**: Display a list of open issues for a specific GitHub repository
- **Command Help**: Built-in help system to guide users on available commands

### Commands

- `!hilfe` - Displays help information about the bot
- `!issue [username/repository] [issue title]` - Creates a link to open a new GitHub issue
- `!show_issues [username/repository]` - Shows up to 10 open issues from a GitHub repository

## Screenshots

### Help Command

![image](https://github.com/user-attachments/assets/b0729fbf-5edf-45f9-a12f-2466dd61b527)


### Issue Creation

![image](https://github.com/user-attachments/assets/7b61c193-f1f2-492b-9454-c3a0978759e8)


### Viewing Repository Issues

![image](https://github.com/user-attachments/assets/b754044f-1846-40b1-a61d-9a47f5ee4f80)


## Current State

This bot is currently in a functional prototype state. It provides basic GitHub issue management capabilities but has room for expansion. The bot currently:

- Uses Discord.py for bot functionality
- Interacts with GitHub's API to fetch issue data
- Provides formatted embeds for better user experience

## Future Development Opportunities

The bot could be enhanced with:

1. **Authentication**: Add GitHub authentication to allow creating issues directly instead of just links
2. **Issue Details**: Allow users to add descriptions, labels, and assignees when creating issues
3. **Issue Comments**: Enable viewing and adding comments to existing issues
4. **Webhook Integration**: Set up notifications in Discord when GitHub issues are updated
5. **Repository Management**: Add commands to manage repositories and view repository statistics
6. **User Settings**: Allow users to set default repositories for quicker issue creation
7. **Slash Commands**: Implement Discord's slash command functionality for better user experience
8. **Error Handling**: Improve error messages and validation for better user feedback

## Installation

1. Clone this repository:

```bash
git clone https://github.com/majdAlmotaem/DiscordBot-GithubIssues.git
```

2. Install required dependencies:

```bash
pip install discord.py requests
```

3. Configure your Discord bot token in the code

4. Run the bot:

```bash
python discord_bot.py
```

## Usage

1. Invite the bot to your Discord server
2. Use `!hilfe` to see available commands
3. Create issues with `!issue [username/repository] [issue title]`
4. View repository issues with `!show_issues [username/repository]`

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues to suggest improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Author

Majd Almotaem
