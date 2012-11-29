# sumTwoNumbers

from behave import *
#
@given('{num01} and {num02}')
def impl(context, num01, num02):
    #print "-->",num01, num02
	context.num01 = int(num01)
	context.num02 = int(num02)

@when('we add both numbers')
def impl(context):
	# No lo suma sino que lo concatena
	context.sum = context.num01 + context.num02

@then('result is {res}')
def impl(context, res):
	print context.sum, res
	assert context.sum is int(res)
	
	
	