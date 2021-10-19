"""This file contains metadata to help describe the featurizers.
"""

properties = {
    "desc3d": {
        "Asphericity" : {
            "name" : "asphericity",
            "dimensionality": "scalar",
            "type": "float",
            "units": "",
            "description": "molecular asphericity",
        },
        "Eccentricity" : {
            "name" : "eccentricity",
            "dimensionality": "scalar",
            "type": "float",
            "units": "",
            "description": "molecular eccentricity",
        },
        "InertialShapeFactor" : {
            "name" : "inertial_shape_factor",
            "dimensionality": "scalar",
            "type": "float",
            "units": "",
            "description": "inertial shape factor",
        },
        "NPR1" : {
            "name" : "npr1",
            "dimensionality": "scalar",
            "type": "float",
            "units": "",
            "description": "Normalized principal moments ratio 1 (=I1/I3)"
        },
        "NPR2" : {
            "name" : "npr2",
            "dimensionality": "scalar",
            "type": "float",
            "units": "",
            "description": "Normalized principal moments ratio 2 (=I2/I3)"
        },
    },
    "desc2d" : {
        "MaxEStateIndex" : {
            "name" : "max_e_state_index",
            "dimensionality": "scalar",
            "type": "float",
            "units": "",
            "description": "maximum value of the electrotopological state atom index"
        },
        "MinEStateIndex" : {
            "name" : "min_e_state_index",
            "dimensionality": "scalar",
            "type": "float",
            "units": "",
            "description": "minimum value of the electrotopological state atom index"
        },
        "MaxAbsEStateIndex" : {
            "name" : "max_abs_e_state_index",
            "dimensionality": "scalar",
            "type": "float",
            "units": "",
            "description": "maximum absolute value of the electrotopological state atom index"
        },
        "MinAbsEStateIndex" : {
            "name" : "min_abs_e_state_index",
            "dimensionality": "scalar",
            "type": "float",
            "units": "",
            "description": "minimum absolute value of the electrotopological state atom index"
        },
        "MolWt" : {
            "name" : "mol_wt",
            "dimensionality": "scalar",
            "type": "float",
            "units": "a.u.",
            "description": "average molecular weight"
        },
    }
}