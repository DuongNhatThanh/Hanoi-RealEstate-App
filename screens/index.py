from screens.collection import Collection_Screen
from screens.exploration import Exploration_Screen
from screens.analysis import Analysis_Screen
from screens.reflection import Reflection_Screen
from screens.search import Search_Property
from utils.index import get_hash

def get_routes():
    screens = [
        {
            "component": Collection_Screen,
            "name": "Collection",
            "icon": "cloud-download"
        },
        {
            "component": Exploration_Screen,
            "name": "Exploration",
            "icon": "folder2"
        },
        {
            "component": Analysis_Screen,
            "name": "Analysis",
            "icon": "bar-chart-line"
        },
        {
            "component": Search_Property,
            "name": "Search",
            "icon": "search"  
        },
        {
            "component": Reflection_Screen,
            "name": "Reflection",
            "icon": "award"
        }
    ]
    
    return get_hash(screens)
