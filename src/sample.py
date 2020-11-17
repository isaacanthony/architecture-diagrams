"""Sample diagram"""
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


def main():
    """Main entrypoint"""
    with Diagram(
        "Sample Architecture Diagram",
        direction="TB",
        filename="img/sample",
        show=False,
    ):
        workers = [EC2(f"EC2\nworker{i + 1}") for i in range(5)]
        ELB("ELB") >> workers >> RDS("RDS\ndata warehouse")


if __name__ == "__main__":
    main()
