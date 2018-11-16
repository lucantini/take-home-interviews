# Carta - Backend take-home interview assignment

## Group Purchase store

You are creating a Checkout system, where a user enters in a Credit Card and then can place an Order.  Our store only carries one type of item, so don’t worry about the type of the items in this order.  We are a group-buying platform, so sometimes Credit cards are "owned" by individuals and sometimes they are "owned" by an OwnerGroup (set of users). A shipping address will also be requested during check-out.

Someone logs in, and is presented with the following screens:
- "Create Order" and "Join Group" buttons
- "Join Group" asks for the group name
- "Create Order" asks for item amount and takes the user to checkout
- Show screen to enter a credit card and billing details
- Enter shipping details

### Other details
- Show user's name and "you are a member of Dunder Mifflin"
- Making someone a group administrator is done via admin interface.

### Application specification:
- Users can create an account with a username+password combination.
- Users can join an OwnerGroup if they know its name.
- Users can create an order for one or more Items and proceed to checkout
- Payment is made with a credit card. Credit card attributes include name, number, CVV, and billing address.
- Purchases can be made either by individuals or by group administrators.
- Shipping address is required to finish the order.
- Show a confirmation screen.

### Project instructions

- Clone this repository on your machine
- Remove the `.git` directory in the repo's root directory
- Initialize a new repository in the `./django_project` directory

Feel free to commit your changes to your new repo as you go. When you're finished, create a new repo on GitHub or GitLab to create a remote and push your code. If you decide to create a private repository, be prepared to add your interviewer as a contributor.
