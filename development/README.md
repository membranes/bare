<br>

## Development Environment

<br>

### Remote Development

For this Python project/template, the remote development environment requires

* [Dockerfile](../.devcontainer/Dockerfile)
* [requirements.txt](../.devcontainer/requirements.txt)

An image is built via the command

```shell
docker build . --file .devcontainer/Dockerfile -t interact
```

On success, the output of

```shell
docker images
```

should include

<br>

| repository | tag    | image id | created  | size     |
|:-----------|:-------|:---------|:---------|:---------|
| interact   | latest | $\ldots$ | $\ldots$ | $\ldots$ |


<br>

Subsequently, run a container, i.e., an instance, of the image `interact` via:

<br>

```shell
docker run --rm --gpus all --shm-size=16gb -i -t 
  -p 7860:7860 -p 8000:8000 -w /app 
    --mount type=bind,src="$(pwd)",target=/app 
      -v ~/.aws:/root/.aws interact
```

<br>

Herein, `-p 7860:7860` maps the host port `7860` to container port `7860`.  Note, the container's working environment, i.e., -w, must be inline with this project's top directory.  Additionally

* --rm: [automatically remove container](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the)
* -i: [interact](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di)
* -t: [tag](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your)
* -p: [publish a container's ports to its host](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s)

<br>

Get the name of the running instance of ``interact`` via:

```shell
docker ps --all
```

Never deploy a root container.

<br>

### Remote Development & Integrated Development Environments

An IDE (integrated development environment) is a helpful remote development tool.  The **IntelliJ
IDEA** set up involves connecting to a machine's Docker [daemon](https://www.jetbrains.com/help/idea/docker.html#connect_to_docker), the steps are

<br>

> * **Settings** $\rightarrow$ **Build, Execution, Deployment** $\rightarrow$ **Docker** $\rightarrow$ **WSL:** {select the linux operating system}
> * **View** $\rightarrow$ **Tool Window** $\rightarrow$ **Services** <br>Within the **Containers** section connect to the running instance of interest, or ascertain connection to the running instance of interest.

<br>

**Visual Studio Code** has its container attachment instructions; study [Attach Container](https://code.visualstudio.com/docs/devcontainers/attach-container).


<br>
<br>

## Devices

An auto method for device selection is

```shell
import logging
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
logging.info('Device: %s', device)
```

<br>
<br>


## Code Analysis

The GitHub Actions script [main.yml](../.github/workflows/main.yml) conducts code analysis within a Cloud GitHub Workspace.  Depending on the script, code analysis may occur `on push` to any repository branch, or `on push` to a specific branch.  The sections herein outline remote code analysis.

### pylint

The directive

```shell
pylint --generate-rcfile > .pylintrc
```

generates the dotfile `.pylintrc` of the static code analyser [pylint](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html).  Analyse a directory via the command

```shell
python -m pylint --rcfile .pylintrc {directory}
```

The `.pylintrc` file of this template project has been **amended to adhere to team norms**, including

* Maximum number of characters on a single line.
  > max-line-length=127

* Maximum number of lines in a module.
  > max-module-lines=135


<br>

### pytest & pytest coverage

The directive patterns

```shell
python -m pytest tests/{directory.name}/...py
pytest --cov-report term-missing  --cov src/{directory.name}/...py tests/{directory.name}/...py
```

for test and test coverage, respectively.

<br>

### flake8

For code & complexity analysis.  A directive of the form

```bash
python -m flake8 --count --select=E9,F63,F7,F82 --show-source --statistics src/...
```

inspects issues in relation to logic (F7), syntax (Python E9, Flake F7), mathematical formulae symbols (F63), undefined variable names (F82).  Additionally

```shell
python -m flake8 --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics src/...
```

inspects complexity.

<br>
<br>

## Snippets

```shell
@staticmethod
def __selection():
    """
    Notes<br>
    -------<br>

    <b>Objective</b>: The wherewithal to click on a highlighted text and correct 
    its tag assignment if it is incorrect.  Subsequently, the corrected piece is 
    saved in alongside the original results; opt for a smart saving option.<br><br>

    def onselect(event: gradio.SelectData): return event.index.<br>
    .select(onselect, inputs=None, outputs=options)<br><br>

    :return:
    """

    gradio.Dropdown(
        ['O', 'B-GEO', 'B-GPE', 'B-TIM', 'B-ORG', 'I-GEO', 'B-PER', 
         'I-PER', 'I-ORG', 'I-TIM', 'I-GPE'],
        interactive=True, label='tags')
```

<br>

```python
import datetime

datetime.datetime.now().strftime('%Y-%m-%d')
```



<br>
<br>

## References

Images:
* [docker hub](https://hub.docker.com)
* [NVIDIA <abbr title="Graphics Processing Unit">GPU</abbr> Cloud (NGC) Catalogue](https://catalog.ngc.nvidia.com)

Interfaces:
* [GRADIO & Docker](https://www.gradio.app/main/guides/deploying-gradio-with-docker)
* [GRADIO Documentation](https://www.gradio.app/docs/gradio/interface)
  * [Named Entity Recognition](https://www.gradio.app/guides/named-entity-recognition)
* [Generators](https://jamstack.org/generators/)
  * [11ty](https://www.11ty.dev)

Amazon:
* [Prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
