{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':u'Chat_Client',
          'size':(628, 318),
          'statusBar':1,
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'StaticText', 
    'name':'StaticText6', 
    'position':(535, 100), 
    'text':u'Port', 
    },

{'type':'StaticText', 
    'name':'StaticText5', 
    'position':(540, 55), 
    'text':u'IP', 
    },

{'type':'StaticText', 
    'name':'StaticText4', 
    'position':(525, 5), 
    'text':u'Buffersize', 
    },

{'type':'StaticText', 
    'name':'StaticText3', 
    'position':(431, 98), 
    'text':u'Port', 
    },

{'type':'StaticText', 
    'name':'StaticText2', 
    'position':(430, 4), 
    'text':u'Nick', 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(439, 51), 
    'text':u'IP', 
    },

{'type':'TextArea', 
    'name':'chathistory', 
    'position':(5, 5), 
    'size':(375, 180), 
    'editable':False, 
    },

{'type':'TextField', 
    'name':'NICK', 
    'position':(391, 20), 
    'toolTip':u'enter Nick', 
    },

{'type':'TextField', 
    'name':'UDP_IP', 
    'position':(390, 69), 
    'toolTip':u'enter the Server IP you want to connect to', 
    },

{'type':'TextField', 
    'name':'UDP_PORT', 
    'position':(390, 115), 
    'toolTip':u'enter the Server Port you want to connect to', 
    },

{'type':'Button', 
    'name':'connect', 
    'position':(401, 143), 
    'size':(81, 30), 
    'label':u'Connect', 
    'toolTip':u'Connect to Server', 
    },

{'type':'Button', 
    'name':'disconnect', 
    'position':(405, 176), 
    'enabled':False, 
    'label':u'Disconnect', 
    'toolTip':u'Disconnect from Server', 
    },

{'type':'TextField', 
    'name':'BUFFERSIZE', 
    'position':(500, 20), 
    'toolTip':u'enter the Buffersize for the Server', 
    },

{'type':'TextField', 
    'name':'IP', 
    'position':(500, 70), 
    'toolTip':u'enter the IP over that the Server should open', 
    },

{'type':'TextField', 
    'name':'PORT', 
    'position':(500, 115), 
    'toolTip':u'enter the Port over that the Server should open', 
    },

{'type':'Button', 
    'name':'startserver', 
    'position':(509, 141), 
    'size':(83, 31), 
    'label':u'Start Server', 
    'toolTip':u'Start the Server', 
    },

{'type':'ToggleButton', 
    'name':'ONLINE', 
    'position':(512, 176), 
    'enabled':False, 
    'label':u'Go Online', 
    'toolTip':u'Switch Online Mode', 
    },

{'type':'TextArea', 
    'name':'chatenter', 
    'position':(7, 191), 
    'size':(300, 40), 
    'enabled':False, 
    },

{'type':'Button', 
    'name':'send', 
    'position':(311, 190), 
    'size':(-1, 43), 
    'enabled':False, 
    'label':u'Send', 
    },

{'type':'Button', 
    'name':'exit', 
    'position':(401, 202), 
    'size':(189, 29), 
    'label':u'Exit', 
    'toolTip':u'Exit', 
    },

] # end components
} # end background
] # end backgrounds
} }
