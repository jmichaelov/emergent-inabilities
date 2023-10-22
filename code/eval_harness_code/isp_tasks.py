"""
Inverse Scaling: When Bigger Isn't Better
https://arxiv.org/abs/2306.09479

10 multiple-choice tasks on which model performance has been found
to decrease as the model's scale increases. 
Note that there is also an 11th task in the paper (not implemented here)
that is based on sequence probability.

https://github.com/inverse-scaling/prize
"""
from lm_eval.base import MultipleChoiceTask



_CITATION = """
@article{mckenzie2023inverse,
  title={Inverse Scaling: When Bigger Isn't Better},
  author={McKenzie, Ian R and Lyzhov, Alexander and Pieler, Michael and Parrish, Alicia and Mueller, Aaron and Prabhu, Ameya and McLean, Euan and Kirtland, Aaron and Ross, Alexis and Liu, Alisa and others},
  journal={arXiv preprint arXiv:2306.09479},
  year={2023}
}
"""


class ISPSigFigs(MultipleChoiceTask):
    VERSION = 0
    DATASET_PATH = "jmichaelov/inverse_scaling_prize-sig_figs"
    DATASET_NAME = None

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return False

    def has_test_docs(self):
        return True

    def training_docs(self):
        if self.has_training_docs():

            if self._training_docs is None:
                self._training_docs = list(
                    map(self._process_doc, self.dataset["train"])
                )
            return self._training_docs

    def validation_docs(self):
        if self.has_validation_docs():
            return map(self._process_doc, self.dataset["validation"])

    def test_docs(self):
        if self.has_test_docs():
            return map(self._process_doc, self.dataset["test"])

    def _process_doc(self, doc):
        return {
            "query": doc["prompt"],
            "choices": doc["classes"].split("'")[1::2],
            "gold": doc["answer_index"],
        }

    def doc_to_text(self, doc):
        return doc["query"]


class ISPResistingCorrection(MultipleChoiceTask):
    VERSION = 0
    DATASET_PATH = "jmichaelov/inverse_scaling_prize-resisting_correction"
    DATASET_NAME = None

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return False

    def has_test_docs(self):
        return True

    def training_docs(self):
        if self.has_training_docs():

            if self._training_docs is None:
                self._training_docs = list(
                    map(self._process_doc, self.dataset["train"])
                )
            return self._training_docs

    def validation_docs(self):
        if self.has_validation_docs():
            return map(self._process_doc, self.dataset["validation"])

    def test_docs(self):
        if self.has_test_docs():
            return map(self._process_doc, self.dataset["test"])

    def _process_doc(self, doc):
        return {
            "query": doc["prompt"],
            "choices": doc["classes"].split("'")[1::2],
            "gold": doc["answer_index"],
        }

    def doc_to_text(self, doc):
        return doc["query"]


class ISPRepetitiveAlgebra(MultipleChoiceTask):
    VERSION = 0
    DATASET_PATH = "jmichaelov/inverse_scaling_prize-repetitive_algebra"
    DATASET_NAME = None

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return False

    def has_test_docs(self):
        return True

    def training_docs(self):
        if self.has_training_docs():

            if self._training_docs is None:
                self._training_docs = list(
                    map(self._process_doc, self.dataset["train"])
                )
            return self._training_docs

    def validation_docs(self):
        if self.has_validation_docs():
            return map(self._process_doc, self.dataset["validation"])

    def test_docs(self):
        if self.has_test_docs():
            return map(self._process_doc, self.dataset["test"])

    def _process_doc(self, doc):
        return {
            "query": doc["prompt"],
            "choices": doc["classes"].split("'")[1::2],
            "gold": doc["answer_index"],
        }

    def doc_to_text(self, doc):
        return doc["query"]



class ISPPatternMatchingSuppression(MultipleChoiceTask):
    VERSION = 0
    DATASET_PATH = "jmichaelov/inverse_scaling_prize-pattern_matching_suppression"
    DATASET_NAME = None

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return False

    def has_test_docs(self):
        return True

    def training_docs(self):
        if self.has_training_docs():
            if self._training_docs is None:
                self._training_docs = list(
                    map(self._process_doc, self.dataset["train"])
                )
            return self._training_docs

    def validation_docs(self):
        if self.has_validation_docs():
            return map(self._process_doc, self.dataset["validation"])

    def test_docs(self):
        if self.has_test_docs():
            return map(self._process_doc, self.dataset["test"])

    def _process_doc(self, doc):
        return {
            "query": doc["prompt"],
            "choices": doc["classes"].split("'")[1::2],
            "gold": doc["answer_index"],
        }

    def doc_to_text(self, doc):
        return doc["query"]


class ISPModusTollens(MultipleChoiceTask):
    VERSION = 0
    DATASET_PATH = "jmichaelov/inverse_scaling_prize-modus_tollens"
    DATASET_NAME = None

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return False

    def has_test_docs(self):
        return True

    def training_docs(self):
        if self.has_training_docs():
            if self._training_docs is None:
                self._training_docs = list(
                    map(self._process_doc, self.dataset["train"])
                )
            return self._training_docs

    def validation_docs(self):
        if self.has_validation_docs():
            return map(self._process_doc, self.dataset["validation"])

    def test_docs(self):
        if self.has_test_docs():
            return map(self._process_doc, self.dataset["test"])

    def _process_doc(self, doc):
        return {
            "query": doc["prompt"],
            "choices": doc["classes"].split("'")[1::2],
            "gold": doc["answer_index"],
        }

    def doc_to_text(self, doc):
        return doc["query"]



class ISPIntoTheUnknown(MultipleChoiceTask):
    VERSION = 0
    DATASET_PATH = "jmichaelov/inverse_scaling_prize-into_the_unknown"
    DATASET_NAME = None

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return False

    def has_test_docs(self):
        return True

    def training_docs(self):
        if self.has_training_docs():
            if self._training_docs is None:
                self._training_docs = list(
                    map(self._process_doc, self.dataset["train"])
                )
            return self._training_docs

    def validation_docs(self):
        if self.has_validation_docs():
            return map(self._process_doc, self.dataset["validation"])

    def test_docs(self):
        if self.has_test_docs():
            return map(self._process_doc, self.dataset["test"])

    def _process_doc(self, doc):
        return {
            "query": doc["prompt"], 
            "choices": doc["classes"].split("'")[1::2], 
            "gold": doc["answer_index"], 
        }

    def doc_to_text(self, doc):
        return doc["query"]




class ISPRedefine(MultipleChoiceTask):
    VERSION = 0
    DATASET_PATH = "jmichaelov/inverse_scaling_prize-redefine"
    DATASET_NAME = None

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return False

    def has_test_docs(self):
        return True

    def training_docs(self):
        if self.has_training_docs():
            if self._training_docs is None:
                self._training_docs = list(
                    map(self._process_doc, self.dataset["train"])
                )
            return self._training_docs

    def validation_docs(self):
        if self.has_validation_docs():
            return map(self._process_doc, self.dataset["validation"])

    def test_docs(self):
        if self.has_test_docs():
            return map(self._process_doc, self.dataset["test"])

    def _process_doc(self, doc):
        return {
            "query": doc["prompt"],
            "choices": doc["classes"].split("'")[1::2],
            "gold": doc["answer_index"],
        }

    def doc_to_text(self, doc):
        return doc["query"]



class ISPNeQA(MultipleChoiceTask):
    VERSION = 0
    DATASET_PATH = "jmichaelov/inverse_scaling_prize-neqa"
    DATASET_NAME = None

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return False

    def has_test_docs(self):
        return True

    def training_docs(self):
        if self.has_training_docs():
            if self._training_docs is None:
                self._training_docs = list(
                    map(self._process_doc, self.dataset["train"])
                )
            return self._training_docs

    def validation_docs(self):
        if self.has_validation_docs():
            return map(self._process_doc, self.dataset["validation"])

    def test_docs(self):
        if self.has_test_docs():
            return map(self._process_doc, self.dataset["test"])

    def _process_doc(self, doc):
        return {
            "query": doc["prompt"],
            "choices": doc["classes"].split("'")[1::2],
            "gold": doc["answer_index"],
        }

    def doc_to_text(self, doc):
        return doc["query"]




class ISPMemoTrap(MultipleChoiceTask):
    VERSION = 0
    DATASET_PATH = "jmichaelov/inverse_scaling_prize-memo_trap"
    DATASET_NAME = None

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return False

    def has_test_docs(self):
        return True

    def training_docs(self):
        if self.has_training_docs():
            if self._training_docs is None:
                self._training_docs = list(
                    map(self._process_doc, self.dataset["train"])
                )
            return self._training_docs

    def validation_docs(self):
        if self.has_validation_docs():
            return map(self._process_doc, self.dataset["validation"])

    def test_docs(self):
        if self.has_test_docs():
            return map(self._process_doc, self.dataset["test"])

    def _process_doc(self, doc):
        return {
            "query": doc["prompt"],
            "choices": doc["classes"].split("'")[1::2],
            "gold": doc["answer_index"],
        }

    def doc_to_text(self, doc):
        return doc["query"]




class ISPHindsightNeglect(MultipleChoiceTask):
    VERSION = 0
    DATASET_PATH = "jmichaelov/inverse_scaling_prize-hindsight_neglect"
    DATASET_NAME = None

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return False

    def has_test_docs(self):
        return True

    def training_docs(self):
        if self.has_training_docs():
            if self._training_docs is None:
                self._training_docs = list(
                    map(self._process_doc, self.dataset["train"])
                )
            return self._training_docs

    def validation_docs(self):
        if self.has_validation_docs():
            return map(self._process_doc, self.dataset["validation"])

    def test_docs(self):
        if self.has_test_docs():
            return map(self._process_doc, self.dataset["test"])

    def _process_doc(self, doc):
        return {
            "query": doc["prompt"],
            "choices": doc["classes"].split("'")[1::2],
            "gold": doc["answer_index"],
        }

    def doc_to_text(self, doc):
        return doc["query"]
