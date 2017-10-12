
for i in range(0,10):
    print "Hello world: " + str(i)
else:
    # This is a useless 'else' branch: it will always be
    # executed because the loop does not have a 'break'
    print "The loop has ended!"

for i in range(0,10):
    print "Hello world: " + str(i)
else:
    # This is a useless 'else' branch, but the alert should be
    # suppressed by lgtm.com
    print "The loop has ended!" # lgtm [py/redundant-else]
