Test file with Sphinx-Needs content
###################################


Examples form another repository
================================

.. stake_req:: Merge python dictionaries
   :id: CSTRQ_MERGE_DICTS
   :author: PhilipPartsch
   :status: accepted

   Provide a python module with a function to merge
   python dictionaries to one dictionary.


.. sw_req:: Definition: list of dictionaries
   :id: SWRQ_LIST_OF_DICTS
   :status: verified
   :satisfies: CSTRQ_MERGE_DICTS

   The above defined function to merge dictionaries shall treat list as:
   none, one, two or many dictionaries organized in a list.

   .. verify:: Test function with appropriate number of dictionaries
      :id: VERIFY_SWRQ_LIST_OF_DICTS

      Test function with:

      - empty list
      - one dictionary in the list
      - two dictionary in the list
      - three dictionary in the list (many)

      With python it is difficult to test the upper bound.


Examples for references
=======================

Here we reference to a need with id CSTRQ_MERGE_DICTS via
:need:`CSTRQ_MERGE_DICTS`.

This shall even work within a need:

.. sw_req:: Reference to a need
   :id: SWRQ_REFERENCE_TO_NEED
   :status: new
   :satisfies: CSTRQ_MERGE_DICTS

   This need shall reference to the need with id CSTRQ_MERGE_DICTS via
   :need:`CSTRQ_MERGE_DICTS`.
