FROM python:3.12-slim

ENV SPARK_VERSION=4.1.1 \
    SPARK_HOME=/opt/spark \
    HADOOP_VERSION=3

WORKDIR $SPARK_HOME

# Install dependencies
RUN apt-get update && \
    apt-get install -y wget openjdk-21-jre

# Install Spark
RUN wget --no-verbose -O apache-spark.tgz "https://dlcdn.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz" \
    && tar -xf apache-spark.tgz -C $SPARK_HOME --strip-components 1 \
    && rm apache-spark.tgz \
    && mkdir -p /tmp/spark-events

ENV PATH=$PATH:$SPARK_HOME/bin

EXPOSE 8080 7077 18080 4040

COPY ./spark-defaults.conf $SPARK_HOME/conf/
