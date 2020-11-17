"""Sample diagram"""
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


def main():
    """Main entrypoint"""
    with Diagram("Sample", show=False, direction="TB", filename="img/sample"):
        ELB("lb") >> [EC2("worker1"),
                      EC2("worker2"),
                      EC2("worker3"),
                      EC2("worker4"),
                      EC2("worker5")] >> RDS("events")


if __name__ == "__main__":
    main()
