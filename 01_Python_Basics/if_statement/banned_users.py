# Checking Whether a Value Is Not in a List

# consider a list of users who are banned from commenting in a forum. You can check
# whether a user has been banned before allowing that person to submit a comment
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, You can post a response if you wish.")
