# Orca
#
# Copyright 2005 Sun Microsystems Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import orca.debug as debug
import orca.default as default
import orca.atspi as atspi
import orca.rolenames as rolenames
import orca.orca as orca
import orca.braille as braille
import orca.speech as speech
import orca.settings as settings
import orca.util as util

from orca.orca_i18n import _ # for gettext support

########################################################################
#                                                                      #
# The planner script class.                                            #
#                                                                      #
########################################################################

class Script(default.Script):

    def __init__(self, app):
        """Creates a new script for the given application.

        Arguments:
        - app: the application to create a script for.
        """

        default.Script.__init__(self, app)


    # This method tries to detect and handle the following cases:
    # 1) Main window: one of the four graphic toggle buttons.

    def onFocus(self, event):
        """Called whenever an object gets focus.

        Arguments:
        - event: the Event
        """

        brailleGen = self.brailleGenerator
        speechGen = self.speechGenerator

        debug.printObjectEvent(debug.LEVEL_FINEST,
                               event,
                               event.source.toString())

        # atspi.printAncestry(event.source)

        # 1) Main window: one of the four graphic toggle buttons.
        #
        # If the focus is on one of the four graphic toggle buttons on
        # the left side of the main window, then get the label associated
        # with it, and speak it.  The reason we do this hack is because
        # planner has not bound the labels to the toggle buttons and we
        # need to do the mapping ourselves.
        #
        # We then do the default action for this focus event, followed by
        # added the label to the braille display.
        #
        # If planner is ever fixed to bind the labels to the toggle buttons,
        # then this code should be removed.
        #
        rolesList = [rolenames.ROLE_TOGGLE_BUTTON, \
                     rolenames.ROLE_FILLER, \
                     rolenames.ROLE_FILLER, \
                     rolenames.ROLE_PANEL, \
                     rolenames.ROLE_PANEL]
        if util.isDesiredFocusedItem(event.source, rolesList):
            debug.println(debug.LEVEL_FINEST,
                      "planner.onFocus - main window: " \
                      + "one of the four graphic toggle buttons.")

            filler = event.source.parent
            allLabels = atspi.findByRole(filler, rolenames.ROLE_LABEL)
            utterance = allLabels[0].name
            speech.speak(utterance)

            default.Script.onFocus(self, event)

            # The region with focus is going to be the toggle button.  We
            # want the entire region to be sensitive to cursor routing keys,
            # so we augment the string for the region with focus with the
            # label we just discovered.
            #
            [brailleRegions, regionWithFocus] = \
                brailleGen.getBrailleRegions(event.source)
            regionWithFocus.string = utterance + " " \
                                     + regionWithFocus.string
            braille.displayRegions([brailleRegions, regionWithFocus]) 
            return


        # For everything else, pass the focus event onto the parent class 
        # to be handled in the default way.

        default.Script.onFocus(self, event)
