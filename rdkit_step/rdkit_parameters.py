# -*- coding: utf-8 -*-
"""
Control parameters for the RDKit step in a SEAMM flowchart
"""

import logging
import seamm
import pprint  # noqa: F401

logger = logging.getLogger(__name__)


class RdkitParameters(seamm.Parameters):
    """
    The control parameters for RDKit.

    The developer will add a dictionary of Parameters to this class.
    The keys are parameters for the current plugin, which themselves
    might be dictionaries.

    You need to replace the "time" example below with one or more
    definitions of the control parameters for your plugin and application.

    Parameters
    ----------
    parameters :
        A dictionary containing the parameters for the current step.
        Each key of the dictionary is a dictionary that contains the
        the following keys: kind, default, default_units, enumeration,
        format_string, description and help text.

    parameters["kind"] : custom
        Specifies the kind of a variable. While the "kind" of a variable might be a
        numeric value, it may still have enumerated custom values meaningful to the
        user. For instance, if the parameter is a convergence criterion for an
        optimizer, custom values like "normal", "precise", etc, might be adequate. In
        addition, any parameter can be set to a variable of expression, indicated by
        having "$" as the first character in the field. For example, $OPTIMIZER_CONV.

    parameters["default"] : "integer" or "float" or "string" or "boolean" or
        "enum" The default value of the parameter, used to reset it.

    parameters["default_units"] : str
        The default units, used for resetting the value.

    parameters["enumeration"] : tuple
        A tuple of enumerated values.

    parameters["format_string"] : str
        A format string for "pretty" output.

    parameters["description"] : str
        A short string used as a prompt in the GUI.

    parameters["help_text"] : tuple
        A longer string to display as help for the user.

    See Also
    --------
    Rdkit, TkRdkit, Rdkit
    RdkitParameters, RDKitStep

    Examples::

        parameters = {
            "time": {
                "default": 100.0,
                "kind": "float",
                "default_units": "ps",
                "enumeration": tuple(),
                "format_string": ".1f",
                "description": "Simulation time:",
                "help_text": ("The time to simulate in the dynamics run.")
            },
        }
    """

    parameters = {
        "features": {
            "default": [],
            "kind": "list",
            "default_units": None,
            "enumeration": tuple(),
            "format_string": "",
            "description": "RDKit Descriptors",
            "help_text": ("The list of RDKit descriptors"),
        },
        "where": {
            "default": "Database",
            "kind": "string",
            "default_units": "",
            "enumeration": ("Database", "Table", "Both"),
            "format_string": "",
            "description": "Where to store the features:",
            "help_text": "Where to store the features",
        },
        "table": {
            "default": "table1",
            "kind": "string",
            "default_units": "",
            "enumeration": None,
            "format_string": "",
            "description": "Table to use:",
            "help_text": "Table to store the features",
        },
    }

    def __init__(self, defaults={}, data=None):
        """
        Initialize the parameters, by default with the parameters defined above

        Parameters
        ----------
        defaults: dict
            A dictionary of parameters to initialize. The parameters
            above are used first and any given will override/add to them.
        data: dict
            A dictionary of keys and a subdictionary with value and units
            for updating the current, default values.

        Returns
        -------
        None
        """

        logger.debug("RdkitParameters.__init__")

        super().__init__(defaults={**RdkitParameters.parameters, **defaults}, data=data)
