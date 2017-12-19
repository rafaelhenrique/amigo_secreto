# Criar chave privada/pública ssh

## No Linux

```
ssh-keygen -t rsa -f ~/.ssh/fs2w
ssh-keygen -t rsa -f ~/.ssh/amigo-secreto-deploy-key
```

## No Windows

- Usando Puttygen: https://www.ssh.com/ssh/putty/windows/puttygen

# Autorizar chave no host remoto

## No Linux

```
ssh-copy-id -i ~/.ssh/fs2w fs2w@<ip do host>
```

## No Windows

- Copie o conteúdo da chave `fs2w.pub`
- Acesse a máquina virtual
- Adicione o conteúdo copiado em /home/fs2w/.ssh/authorized_keys
- Teste o acesso por chave

# Comandos para instalar pré-requisitos

```
ansible virtualbox -i secret/hosts -m raw -a 'apt-get update' -b
ansible virtualbox -i secret/hosts -m raw -a 'apt-get install -y python' -b
```

# Rodar playbook Ansible

```
ansible-playbook <playbook> -v
```