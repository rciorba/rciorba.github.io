The why:

If you're doing anything python web related chances are you've got a fuzzy deployment story.

What do i mean by fuzzy:
 Do you have a concept of a release? Or do you always just run whatever the latest version of code you've got?
 Do you have the concept of a build (code + dependencies) or do you deploy your code as text and compile it on the machine.
 Are your build reproducible? Git tags arent builds
 How about your dependencies? If you rebuild last weeks build, are you sure you get the exact same output?
 If yes? Can you deploy the exact version of code you've tested to on one environmet to a productin environment?