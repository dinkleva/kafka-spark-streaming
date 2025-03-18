# Kafka-Spark-Streaming Project 🚀

## 📌 Overview
This project demonstrates a real-time data processing pipeline using **Kafka**, **Spark Streaming**, **Docker**, and **Grafana** for visualization. Messages are produced to Kafka topics, consumed by Spark Streaming workers, and then displayed in Grafana.

## 📁 Project Structure
```
kafka-spark-streaming/
│── docker-compose.yml        # Defines all services (Kafka, Zookeeper, Spark, Grafana)
│── event.txt                 # Sample event messages in JSON format
│── kafka_producer.py         # Python Kafka Producer script
│── spark_streaming.py        # Spark Streaming Consumer script
│── grafana_dashboard.json    # Grafana dashboard configuration
│── README.md                 # Documentation
```

## ⚙️ Technologies Used
- **Apache Kafka** → Message broker  
- **Apache Spark (PySpark)** → Stream processing  
- **Docker & Docker-Compose** → Containerized setup  
- **Grafana** → Data visualization  
- **Python** → Producer & Consumer scripts  

## 🛠️ Setup and Installation
### 1️⃣ Clone the Repository
```bash
git clone git@github.com:dinkleva/kafka-spark-streaming.git
cd kafka-spark-streaming
```

### 2️⃣ Start the Dockerized Services
```bash
docker-compose up -d
```
This will start:
- **Kafka & Zookeeper**  
- **Spark Cluster (1 Master + 3 Workers)**  
- **Grafana for visualization**  

## 📝 Producing Messages to Kafka
Edit `event.txt` with JSON messages and produce them:  
```bash
cat event.txt | docker exec -i kafka kafka-console-producer.sh --topic events --bootstrap-server kafka:9092
```
✅ **Verify Production:**  
```bash
docker exec -it kafka kafka-console-consumer.sh --topic events --from-beginning --bootstrap-server kafka:9092
```

## 🎯 Running Spark Streaming Consumer
To start Spark consumer:  
```bash
docker exec -it spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/spark_streaming.py
```
✅ **Output:** Processed messages from Kafka displayed in the console.  

## 📊 Visualizing Data in Grafana
- Open Grafana at: [http://localhost:3000](http://localhost:3000)  
- Default login:
  - **Username:** `admin`
  - **Password:** `admin`
- Configure **Spark streaming output** as a data source.  
- Import `grafana_dashboard.json`.  

## 🐛 Troubleshooting
### Kafka is not producing messages
```bash
docker logs kafka
```
Check for **broker errors** in logs.

### Spark can't connect to Kafka
Check the network:
```bash
docker exec -it spark-master ping kafka
```
If unreachable, update `docker-compose.yml` with correct service names.

## 🛠️ Optimizing Message Handling
- **Partitioning Kafka Topics** → Distributes load across consumers  
- **Scaling Spark Executors** → `docker-compose scale spark-worker=5`  
- **Using Kafka Consumer Groups** → Multiple consumer workers  
- **Batching & Windowing in Spark** → Optimized data processing  

## 📌 Next Steps
- **📥 Push new features**
- **🚀 Deploy on Kubernetes**
- **📈 Monitor with Prometheus**
- **⏳ Optimize message latency**

## 👨‍💻 Author
🚀 **Dinkleva** - Passionate about **Data Engineering & Streaming Architectures**  
📧 Contact: `dinkleva@example.com`

✅ **Star this repo** ⭐ if you found it helpful!  
