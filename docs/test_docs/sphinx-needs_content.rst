Test file with Sphinx-Needs content
###################################

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
