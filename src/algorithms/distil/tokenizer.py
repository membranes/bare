"""Module tokenizer"""
import transformers


class Tokenizer:
    """
    Class Tokenizer: <a href="https://arxiv.org/abs/1910.01108" target="_blank">Distil BERT</a>
     (Bidirectional Encoder Representations from Transformers)
    """

    def __init__(self, pretrained_model_name_or_path: str):
        """

        :param pretrained_model_name_or_path: The model's original/standard name<br>
        """

        self.__pretrained_model_name_or_path = pretrained_model_name_or_path

    def __call__(self) -> transformers.tokenization_utils_base.PreTrainedTokenizerBase:
        """

        :return:
        """

        # Tokenizer
        return transformers.DistilBertTokenizerFast.from_pretrained(
            pretrained_model_name_or_path=self.__pretrained_model_name_or_path,
            clean_up_tokenization_spaces=True)
