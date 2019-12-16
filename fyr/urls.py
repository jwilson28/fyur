from django.urls import path
from fyr import views

app_name='fyr'
urlpatterns = [
    path('', views.index, name='index'),
    path('comments/', views.comment, name='comment'),
    path('event_detail/<event_id>/', views.event_detail, name='event_detail'),
    path('event/add', views.add_event, name='add_event'),
    path('addresses/', views.address_list, name ='address_list'),
    path('address_list/add/', views.add_address, name ='add_address'),
    path('bands/', views.band_list, name='band_list'),
    path('bands/add/', views.add_band, name='add_band'),
    path('venues/', views.venue_list, name='venue_list'),
    path('venues/add', views.add_venue, name='add_venue'),
]


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    """
    Linked list should support:
    1. Setting head
    2. Setting tail
    3. Inserting before a given node
    4. Inserting after a given node
    5. Inserting a node at a given position
    6. Removing given nodes
    7. Removing nodes with given values
    8. Removing nodes with
    """

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, node):
        if not self.head:
            self.head = node
            return
        if not self.tail:
            self.tail = node
            self.head.next = node
            self.tail.prev = self.head
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        return

    def print_this(self):
        ll = ""
        if not self.head:
            print(ll, "- empty linked list!")
            return
        curr = self.head
        while curr:
            ll += f"{str(curr.value)}-"
            curr = curr.next
        print(ll[:-1])
        return

a = LinkedList()
for letter in "Portugal":
    #print(letter)
    a.append(Node(letter))
a.print_this()