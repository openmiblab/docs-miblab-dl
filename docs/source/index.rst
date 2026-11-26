#############################
**miblab-dl** documentation
#############################

.. grid:: 1 1 2 2
   :gutter: 3
   :padding: 0
   :class-container: landing-hero

   .. grid-item::
      :columns: 12

      .. admonition:: Purpose
         :class: note

         A Python interface for deep learning models trained by `miblab.org <https://miblab.org>`_.

.. rubric:: Getting Started

.. grid:: 1 3 3 3
   :gutter: 3
   :padding: 0
   :class-container: metadata-footer

   .. grid-item-card:: 📦 Installation
      :class-card: metadata-card

      .. code-block:: console

         pip install miblab-dl

   .. grid-item-card:: 📚 Reference Guide
      :link: reference/index
      :link-type: doc
      :class-card: action-card sd-bg-light
      :text-align: center

      List of functions for model inference in 
      batch mode or case-by-case. 

   .. grid-item-card:: 💻 Examples Gallery
      :link: examples/index
      :link-type: doc
      :class-card: action-card sd-bg-light
      :text-align: center

      Real-world examples for each model, 
      using demo data included in the package.


.. rubric:: About

.. grid:: 1 1 3 3
   :gutter: 4
   :padding: 0
   :class-container: metadata-footer

   .. grid-item-card:: 📜 Citing
      :class-card: metadata-card

      When you use ``miblab-dl`` in your research, please cite:

      .. code-block:: text

         Periquito, J., Thomas, A., Ariens, B., & Sourbron, S. (2026).
         Python API for miblab's Trained Deep-Learning Models (Version v0.0.17).
         Zenodo. https://doi.org/10.5281/zenodo.24565447

   .. grid-item-card:: 🔓 License
      :class-card: metadata-card

      ``miblab-dl`` is distributed under the `Apache 2.0 <https://www.apache.org/licenses/LICENSE-2.0>`_ license.

      A permissive, free license that allows users to freely use, modify, and distribute the software with minimal restrictions.

   .. grid-item-card:: 👥 Maintainers
      :class-card: metadata-card

      ``miblab-dl`` is maintained by the University of Sheffield's medical imaging biomarkers laboratory `miblab.org <https://miblab.org>`_.

.. toctree::
   :maxdepth: 2
   :hidden:

   reference/index
   examples/index